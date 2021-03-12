from graphics import *
import math 

def in_f():
    w = eval(input("Enter the coefficient of x-cube: "))
    r = eval(input("Enter the coefficient of x-squared: "))
    x = eval(input("Enter the coefficient of x in the linear equation you want to graph: "))
    y = eval(input("Enter the Constant of the linear function : "))

    x_val=[]
    y_val=[]
    it = -10
    
    
    while it != 10.5:
        x_val.append(it)
        it += 0.5
    
    for i in x_val:
        f_x = w*(i**3)+r*(i**2)+(x*i)+y
        y_val.append(f_x)
        
    lq,lw,le,lr,lt,ly,lu,li,lo,lp,la,ls,ld,lf,lg,lh,lj,lk,ll,lz,lx,lc,lv,lb,ln,lm,qq,ww,ee,rr,tt,yy,uu,ii,oo,pp,aa,ss,dd,ff,gg = y_val

##    he_val = -20
##    for pair in y_val:
##        print(he_val," ",pair)
##        he_val = he_val + 2 

    win = GraphWin(("Graph "),800,700)
    win.setCoords(-20,-20,20,20)
    win.setBackground("White")
    opp = Line(Point(0,-20),Point(0,20)).draw(win)
    opp.setFill("Green")
    ppo = Line(Point(-20,0),Point(20,0)).draw(win)
    ppo.setFill("Green")
    a,b,c = -0.15,0.15,-20

    for j in range(21):
        Line(Point(a,c),Point(b,c)).draw(win)
        Line(Point(c,a),Point(c,b)).draw(win)
        Text(Point(-0.5,c),c).draw(win)
        Text(Point(c,-0.5),c).draw(win)
        c = c + 2
    if r == 0:
        Line(Point(-20,2*lq),Point(20,2*gg)).draw(win)

    else:

        Polygon(Point(-10,lq),Point(-9.5,lw),Point(-9,le),Point(-8.5,lr),Point(-8,lt),Point(-7.5,ly),Point(-7,lu),Point(-6.5,li),Point(-6,lo),Point(-5.5,lp),Point(-5,la),Point(-4.5,ls),Point(-4,ld),Point(-3.5,lf),Point(-3,lg),Point(-2.5,lh),Point(-2,lj),Point(-1.5,lk),Point(-1,ll),Point(-0.5,lz),Point(0,lx),Point(0.5,lc),Point(1,lv),Point(1.5,lb),Point(2,ln),Point(2.5,lm),Point(3,qq),Point(3.5,ww),Point(4,ee),Point(4.5,rr),Point(5,tt),Point(5.5,yy),Point(6,uu),Point(6.5,ii),Point(7,oo),Point(7.5,pp),Point(8,aa),Point(8.5,ss),Point(9,dd),Point(9.5,ff),Point(10,gg)).draw(win)

        c = str(round((-x+math.sqrt((x**2)-(4*r*y)))/(2*r),2))
        d = str(round((-x-math.sqrt((x**2)-(4*r*y)))/(2*r),2))
        l_sym = str(round((-x/2*r),2))
        m_val = str(round(((4*r*y)-(x**2))/4*r,2))

        if r < 0:
            Text(Point(12,-14),"Maximum value = "+m_val).draw(win)
        else:
            Text(Point(12,-14),"Minimum value = "+m_val).draw(win)

        if c==d:
            Text(Point(12,-13),"Solution Set: x= "+c).draw(win)
        else:     
            Text(Point(12,-13),"Solution Set: x= "+c+" or  x= "+d).draw(win)

        Text(Point(12,-15),"Line of Symmetry: x= "+l_sym).draw(win)

    win.getMouse()
    win.close()
        
in_f()
