function [Mh, DampSp, stiff, Vs, x, dT, Da, Dy, Dw, bigamma, undamp, bmw] = alldataNL(N,dT,Fo,alpha,base);
%  function [Mh, DampsSp, stiff, Vs, x, dT, Da, Dy, Dw, bigamma, undamp] =
% alldataNL(N,Fo,alpha,base);
% 	Function ALLDATANL is called by the main routine in order to load 
%   all data being necessary to the frequency domain implementation of the human cochlea
%    
%	 x  =	BM point vector (nonuniform (function vargrid1(N))
%    Gs =	Stapes propagator multiplayed by the inverse of the Green's function
%	 G =	  the Green's function
%	 DampSp = BM damping matrix accounting for absolute and shear viscosity
%	 stiff = BM stiffness vector
%	 undamp = undamping vector
%	 wm2 =	TM normalized stiffness (K/M)
%	 bigamma =	TM normalized damping   (H/M)
if nargin<5, base=2.2022;    end
if nargin<4, alpha=-7.3094;  end
if nargin<3, Fo=2.0899e+004; end
% Fo=2.0899e+004;


%________________________BM data_______________________________
% if exist('bmdataNL.mat')==2,
% 	load bmdataNL.mat
% else,
	x = gaussgrid(N);  % Generates a set of points covering the interval 0-1 with Gaussian distributed density    (see GAUSSGRID.M) 
    bmdataNL(x);
    load bmdataNL.mat
% end



Ginv = inv(G + M);

Stiff=diag(stiff);

GinvStiff=Ginv*Stiff;

U=diag(ones(size(x)));



GinvDamp = Ginv*ShSp;

Factor=inv(U + GinvDamp*dT + GinvStiff*dT^2);


Mh = Factor*Ginv;

BMinput = Ginv*Gs';

Vs = Factor*BMinput;

DampSp=sparse((Stiff*dT)) + ShSp; % the Laplacian-like matrix ShSp is sparse


%________________________________________________
%  load LAMBDAS6a.mat lam
%  
%  lam = resample(lam,length(x),length(lam)); % lam is natively 600 point vector
%  
% shaping of the amplification
% xx = 10*(1-x(1:200));
% lam = [10.^(xx/20); ones(size(x(201:300)))];

% lam = ones(size(x));
% lam1 = linspace(1.13,1.1,100)'; % higher amplification in higher sections
% lam2 = linspace(1.1,1,100)';
% lam = [lam1; lam2; ones(length(x)-length(lam1)-length(lam2),1)];
lam = linspace(1,1,round(1/2*length(x)))'; % higher amplification in higher sections
% lam = linspace(0.2,1,round(1/2*length(x)))'; % higher amplification in higher sections
lam = [lam; 1.0*ones(length(x)-length(lam),1)];

 %--------------------TM-parameters-----------
 %-------------------------------------------
  wm=2*pi*Fo*base.^(alpha*(x+0.05));
  wm2=wm.*wm;  % equivalent to K/M along the TM 
  bigamma=2*pi*Fo*base.^(0.5*alpha*(x+0.05));
  bigamma=bigamma(:)./0.95;
  wm2=wm2(:);% equivalent to H/M along the TM 
  undamp=1*0.87*damp0.*bigamma.*lam*1;
  % 0.37 def
  undamp=undamp(:);
  stiff=stiff(:);

u=ones(size(x));
 
FactorTM = u./(1 + bigamma*dT + wm2*dT^2);

disp('	Computing Da ...');
Da = FactorTM; % TM-BM coupling constant is set to 1

disp('	Computing Dy ...');
Dy = FactorTM.*wm2;

disp('	Computing Dw ...');
Dw = FactorTM.*(bigamma + wm2*dT)/1.0;


%------------------
Da=Da(:);	% make sure that are columns
Dy=Dy(:);
Dw=Dw(:);

bigamma=bigamma(:);

