clc
clear all
close all
fontsize = 12;


%% Import data
%Training dataset
D11 = dlmread('C:\Users\joud\Documents\Github\UofSC-walking-bridges\Bridge_A\Test Data\Roller excitation response test\sensor nodes\p1\001.CSV',',',0);
D12 = dlmread('C:\Users\joud\Documents\Github\UofSC-walking-bridges\Bridge_A\Test Data\Roller excitation response test\sensor nodes\p2\001.CSV',',',0);
D13 = dlmread('C:\Users\joud\Documents\Github\UofSC-walking-bridges\Bridge_A\Test Data\Roller excitation response test\sensor nodes\p3\001.CSV',',',0);
%D14 = dlmread('C:\Users\joud\Documents\Github\UofSC-walking-bridges\Bridge_A\Test Data\Bridge impulse response test\sensor nodes\p1\000.CSV',',',0);



%% Extract data
EndCut=19000;

tt0=D11(:,1); %Timestamp
dd0=D11(:,2); %Acc (g)
tt0=tt0(1:end-EndCut,:);
dd0=dd0(1:end-EndCut,:);
dd0 = (dd0-mean(dd0))*9.80665; %Acc (m/s^2) 

tt1=D12(:,1); %Timestamp
dd1=D12(:,2); %Acc (g)
tt1=tt1(1:end-EndCut,:);
dd1=dd1(1:end-EndCut,:);
dd1 = (dd1-mean(dd1))*9.80665; %Acc (m/s^2) 
 
tt2=D13(:,1); %Timestamp
dd2=D13(:,2); %Acc (g)
tt2=tt2(1:end-EndCut,:);
dd2=dd2(1:end-EndCut,:);
dd2 = (dd2-mean(dd2))*9.80665; %Acc (m/s^2) 

% ttR=D14(:,1); %Timestamp
% ddRef0=D14(:,2); %Acc (g)
% ddRef1=D14(:,3); %Acc (g)
% ddRef2=D14(:,4); %Acc (g)
% ddRef0 = (ddRef0-mean(ddRef0))*9.80665; %Acc (m/s^2) 
% ddRef1 = (ddRef1-mean(ddRef1))*9.80665; %Acc (m/s^2) 
% ddRef2 = (ddRef2-mean(ddRef2))*9.80665; %Acc (m/s^2) 

%% Interpolate to Timescale

%Package sampling
Fs=400;
Ts=1/Fs;
End=tt0(length(dd0));
tt=Ts: 1/Fs : End; %time column for Fs=400Hz

dd0 = interp1(tt0,dd0,tt);
tt0=tt;
dd1 = interp1(tt1,dd1,tt);
tt1=tt;
dd2 = interp1(tt2,dd2,tt);
tt2=tt;

%Reference Sampling
% Fs=400;
% Ts=1/Fs;
% End=ttR(length(ddRef0));
% ttRef=Ts: 1/Fs : End; %time column for Fs=400Hz

% ddRef0 = interp1(ttR,ddRef0,ttRef);
% ddRef1 = interp1(ttR,ddRef1,ttRef);
% ddRef2 = interp1(ttR,ddRef2,ttRef);

%% Low-Pass Filter
Fcut=20;
dd0=lowpass(dd0,[Fcut],Fs);
dd1=lowpass(dd1,[Fcut],Fs);
dd2=lowpass(dd2,[Fcut],Fs);

% ddRef0=lowpass(ddRef0,[Fcut],Fs);
% ddRef1=lowpass(ddRef1,[Fcut],Fs);
% ddRef2=lowpass(ddRef2,[Fcut],Fs);
%% FFT
Ts0=tt0(2)-tt0(1);
F0Hz=1/Ts0;
Fs0=2*pi*F0Hz; %Rads/s
L0 = length(tt0);% Length of signal

Ts1=tt1(2)-tt1(1);
F1Hz=1/Ts1;
Fs1=2*pi*F1Hz; %Rads/s
L1 = length(tt1);% Length of signal

Ts2=tt2(2)-tt2(1);
F2Hz=1/Ts2;
Fs2=2*pi*F2Hz; %Rads/s
L2 = length(tt2);% Length of signal

% TsRef=ttRef(2)-ttRef(1);
% FRefHz=1/TsRef;
% FsRef=2*pi*FRefHz; %Rads/s
% LRef = length(ttRef);% Length of signal

%Training
%A0 FFT
YA0 = fft(dd0);           
PA02 = abs(YA0/L0);
PA0 = PA02(1:L0/2+1);
PA0(2:end-1) = 2*PA0(2:end-1);
fA0 = (Fs0*(0:(L0/2))/L0)/(2*pi); 

%A1 FFT
YA1 = fft(dd1);           
PA12 = abs(YA1/L1);
PA1 = PA12(1:L1/2+1);
PA1(2:end-1) = 2*PA1(2:end-1);
fA1 = (Fs1*(0:(L1/2))/L1)/(2*pi); 

%A2 FFT
YA2 = fft(dd2);           
PA22 = abs(YA2/L2);
PA2 = PA22(1:L2/2+1);
PA2(2:end-1) = 2*PA2(2:end-1);
fA2 = (Fs2*(0:(L2/2))/L2)/(2*pi); 

% %Ref A0 FFT
% YRef0 = fft(ddRef0);           
% PRef2 = abs(YRef0/LRef);
% PRef0 = PRef2(1:LRef/2+1);
% PRef0(2:end-1) = 2*PRef0(2:end-1);
% fRef0 = (FsRef*(0:(LRef/2))/LRef)/(2*pi); 
% 
% %Ref A1 FFT
% YRef1 = fft(ddRef1);           
% PRef12 = abs(YRef1/LRef);
% PRef1 = PRef12(1:LRef/2+1);
% PRef1(2:end-1) = 2*PRef1(2:end-1);
% fRef1 = (FsRef*(0:(LRef/2))/LRef)/(2*pi); 
% 
% %Ref A3 FFT
% YRef2 = fft(ddRef2);           
% PRef22 = abs(YRef2/LRef);
% PRef2 = PRef22(1:LRef/2+1);
% PRef2(2:end-1) = 2*PRef2(2:end-1);
% fRef2 = (FsRef*(0:(LRef/2))/LRef)/(2*pi); 

% Average FFT power
Avg =150;

%PA0 = movmean(PA0,Avg);
%PA1 = movmean(PA1,Avg);
%PA2 = movmean(PA2,Avg);

% PRef0 = movmean(PRef0,Avg);
% PRef1 = movmean(PRef1,Avg);
% PRef2 = movmean(PRef2,Avg);
%  


%% PLOT 1: Time and frequency domain of Package network
figure(1);
%time domain of training dataset
subplot(2,1,1);
plot(tt0-1,dd0,tt1-1,dd1,tt2-1,dd2);
xlim([0,6.5]);
%ylim([-2,2])
grid on
%title('network time domain');
xlabel("time (s)");
ylabel("acceleration (m/s^2) ");
legend("A0","A1","A2",'Location','northeast');
set(gca,'fontname','times','fontsize',fontsize)  % Set it to times

%Frequency domain of traing dataset
subplot(2,1,2);
%semilogx(fA0,10*log10(PA0),fA1,10*log10(PA1),fA2,10*log10(PA2),'LineWidth',2);
plot(fA0,(PA0),fA1,(PA1),fA2,(PA2),'LineWidth',2);
grid on
%title('network frequency domain');
xlabel('frequency (Hz)');
ylabel('|G(f)|');
legend("A0","A1","A2", 'Location','northeast');
xlim([0,45]);
%ylim([-60,-15]);



x0=100;
y0=300;
width=700;
height=470;


set(gcf,'position',[x0,y0,width,height])
set(gca,'fontname','times','fontsize',fontsize)  % Set it to times


f=figure(1);
exportgraphics(f,'Bridge.png','Resolution',1000)