%-----------------------------------------------------------------------
% Joint Department of Biomedical Engineering
% North Carolina State University
% University of North Carolina - Chapel Hill
% BME 302 Windkessel Lab
% Instructors:
% Dr. Donald O. Freytes
% 
% Name: Jacob Gerlach
% Date: 2/3/2022
%-----------------------------------------------------------------------

clear variables;
clc;

%% Declared variables
HR  70; % BPM
T = 60/HR; % Duration of Cardiac Cycle in sec
Ts =(2/5)*T; % Duration of systole in sec
P0 = 0; % Initial pressure in mmHg

R = 1.05; % Systemic peripheral resistance
C = 1.37;  % Systemic arterial compliance
r = 0.057; % Aortic/pulmonary resistance
L = 0.007; % Total arterial inertance

%% Equations needed to caculate aortic flow
syms ti q
I0 = solve(90-int(q*(sin(pi*ti/Ts)),ti ,0,Ts),q); 
I0 = subs(I0, pi, 3.14);
Io = double(I0);

% Using solution to create input for Simulink models
SampleRate = 0.001;
tOnePeriod = 0:SampleRate:(T-SampleRate);
yOnePeriod = zeros(1,numel(tOnePeriod));
yOnePeriod(tOnePeriod<=Ts) = Io*(sin(pi*tOnePeriod(tOnePeriod<=Ts)/Ts).^2);
simin.time=[];
simin.signals.values=yOnePeriod(:);
simin.signals.dimenions = [1 1];

% Run model
time_duration = 5;% Secs to run simulation
results=sim('Windkessel_Circuit',time_duration);

% Collecting Data for Windkessel models
% Just Resistance
yt0=results.PressureData.signals.values;
tt0=results.PressureData.time;
% 2-Elements Windkessel models
yt1=results.PressureData1.signals.values;
tt1=results.PressureData1.time;
% 3-Elements Windkessel models
yt2=results.PressureData2.signals.values;
tt2=results.PressureData2.time;
% 4-Elements Windkessel models
yt3=results.PressureData3.signals.values;
tt3=results.PressureData3.time;

% Write 1-element and 2-element data to Excel
xlswrite('testing222.xlsx', [tt0, yt0, tt1, yt1]);

% Plot 1-element vs. 2-element
fig = figure();
plot(tt0, yt0, tt1, yt1, "LineWidth",3)
ylabel("Pressure (mmHg)",'FontSize',20)
xlabel("Time (sec)",'FontSize',20)
legend('1-Element', '2-Elements', 'FontSize', 16)
title("1-Element vs. 2-Element Windkessel Simulations",'FontSize',24)
saveas(fig, 'question3.png')


plot([0.001 10000], casson_y*ones(2), casson_x*ones(2))