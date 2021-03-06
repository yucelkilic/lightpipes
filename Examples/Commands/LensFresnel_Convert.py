from LightPipes import *
import matplotlib.pyplot as plt

def TheExample(N):
    fig=plt.figure(figsize=(11,9.5))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    labda=1000*nm;
    size=10*mm;
    
    f1=10*m
    f2=1.11111111*m
    z=1.0*m
    w=5*mm;
    F=Begin(size,labda,N);
    F=RectAperture(w,w,0,0,0,F);
    
#1) Using Lens and Fresnel:
    F1=Lens(z,0,0,F)
    F1=Fresnel(z,F1)
    phi1=Phase(F1);phi1=PhaseUnwrap(phi1)
    I1=Intensity(0,F1);
    x1=[]
    for i in range(N):
        x1.append((-size/2+i*size/N)/mm)  
    
#2) Using Lens + LensFresnel and Convert:
    F2=Lens(f1,0,0,F);
    F2=LensFresnel(f2,z,F2);
    F2=Convert(F2);
    phi2=Phase(F2);phi2=PhaseUnwrap(phi2)
    I2=Intensity(0,F2);
    x2=[]
    newsize=size/10
    for i in range(N):
        x2.append((-newsize/2+i*newsize/N)/mm)

    ax1.plot(x1,phi1[int(N/2)],'k--',label='Lens + Fresnel')
    ax1.plot(x2,phi2[int(N/2)],'k',label='LensFresnel + Convert');
    ax1.set_xlim(-newsize/2/mm,newsize/2/mm)
    ax1.set_ylim(-2,4)
    ax1.set_xlabel('x [mm]');
    ax1.set_ylabel('phase [rad]');
    ax1.set_title('phase, N = %d' %N)
    legend = ax1.legend(loc='upper center', shadow=True)
    
    ax2.plot(x1,I1[int(N/2)],'k--',label='Lens+Fresnel')
    ax2.plot(x2,I2[int(N/2)], 'k',label='LensFresnel + Convert');
    ax2.set_xlim(-newsize/2/mm,newsize/2/mm)
    ax2.set_ylim(0,1000)
    ax2.set_xlabel('x [mm]');
    ax2.set_ylabel('Intensity [a.u.]');
    ax2.set_title('intensity, N = %d' %N)
    legend = ax2.legend(loc='upper center', shadow=True)
    
    ax3.imshow(I1);ax3.axis('off');ax3.set_title('Intensity, Lens + Fresnel, N = %d' %N)
    ax3.set_xlim(int(N/2)-N/20,int(N/2)+N/20)
    ax3.set_ylim(int(N/2)-N/20,int(N/2)+N/20)
    ax4.imshow(I2);ax4.axis('off');ax4.set_title('Intensity, LensFresnel + Convert, N = %d' %N)
    plt.show()

TheExample(100) #100 x 100 grid

TheExample(1000) #1000 x 1000 grid
