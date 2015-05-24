#We build rockets!
import math

class Part:
    """Superclass for any piece of a rocket.

    Methods
    -------
    __init__

    Instance Variables
    ------------------
    name : str
       Identifying name of the part.

    mass : float
       Mass of the part.

    cost : int
       Cost of the part.

    Cd : float
       Drag coefficient of the part.
    """

    def __init__(self, name, m, cost, Cd):
        """Prepare all Part instance variables.

        Returns
        -------
        None

        Parameters
        ----------
        name : str
           Identifying name of the Part.

        m : float
           Mass of the Part.

        cost : int
           Cost of the Part.

        Cd : float
           Drag coefficient of the Part.

        Notes
        -----
        """
        self.name = name
        self.mass = m
        self.cost = cost
        self.Cd = Cd

class Payload(Part):
    """Subclass of Part object distinguished by the addition of power required.

    Methods
    -------
    __init__

    Instance Variables
    ------------------
    pwrRqd : float
       Specifies power required to run the Payload. Can also specify power
      generated by the payload if the number is negative.
    """

    def __init__(self, name, m, cost, Cd, pwrRqd):
        """Prepare all Payload instance variables.

        Returns
        -------
        None

        Parameters
        ----------
        name : str
           Identifying name of the Payload.

        m : float
           Mass of the Payload.

        cost : int
           Cost of the Payload.

        Cd : float
           Drag coefficient of the Payload.

        pwrRqd : float
           Power required to run the Payload. Use a negative number to specify
           power generated by Payload.

        Notes
        -----
        Essentially this will be any object in the rocket that simply uses (or
        generates power). So this could be things like crew cabins, batteries,
        solar panels, etc.
        """
        Part.__init__(self, name, m, cost, Cd)
        self.pwrRqd = pwrRqd

class Engine(Part):
    """Subclass of Part object distinguished by addition of propulsion values.

    Methods
    -------
    __init__

    Instance Variables
    ------------------
    Itot : float
       Total impulse available to impart in newton-seconds.

    Isp : float
       Specific impulse available to impart for this Engine in seconds.

    FvsT : function
       Function which returns the force exerted by the Engine (in Newtons) when
       a time (in seconds) after Engine ignition is passed into it. The time
       argument must accept only a float and the return value must be a float.

    delT : float
       Time (in seconds) since Engine first started being used by the Rocket.go
       method. Think of it as the time since the Engine was ignited (really only
       applies to the solid booster philosophy right now).
    """

    def __init__(self, name, m, cost, Cd, Itot, Isp, FvsT):
        """Prepare all Engine instance variables.

        Returns
        -------
        None

        Parameters
        ----------
        name : str
           Identifying name of the Engine.

        m : float
           Mass of the Engine.

        cost : int
           Cost of the Engine.

        Cd : float
           Drag coefficient of the Engine.

        Itot : float
           Total impulse available to impart in newton-seconds.

        Isp : float
           Specific impulse available to impart for this Engine in seconds.

        FvsT : function
           Function which returns the force exerted by the Engine (in Newtons)
           when a time (in seconds) after Engine ignition is passed into it. The
           time argument must accept only a float and the return value must be a
           float.

        Notes
        -----
        """
        Part.__init__(self, name, m, cost, Cd)
        self.Itot = Itot
        self.Isp  = Isp
        self.FvsT = FvsT
        self.delT = 0.0

class Fueltank(Part):
    """Subclass of Part object distinguished by the addition of dry mass value.

    Methods
    -------
    __init__

    Instance Variables
    ------------------
    drymass : float
       Mass of tank when it is empty. This way Fueltank.m minus drymass is the
       mass of the fuel.
    """

    def __init__(self, name, mTot, cost, Cd, drymass):
        """Prepare all Fueltank instance variables.

        Returns
        -------
        None

        Parameters
        ----------
        name : str
           Identifying name of the Fueltank.

        mTot : float
           Mass of the Fueltank when full.

        cost : int
           Cost of the Fueltank.

        Cd : float
           Drag coefficient of the Fueltank.

        drymass : float
           Mass of the Fueltank when empty.

        Notes
        -----
        """
        Part.__init__(self, name, mTot, cost, Cd)
        self.drymass = drymass

class Decoupler(Part):
    """Subclass of Part object not yet distinguished in any way.

    Methods
    -------
    __init__

    Instance Variables
    ------------------
    """
    def __init__(self, name, m, cost, Cd):
        """Prepare all Decoupler instance variables.

        Returns
        -------
        None

        Parameters
        ----------
        name : str
           Identifying name of the Decoupler.

        m : float
           Mass of the Decoupler.

        cost : int
           Cost of the Decoupler.

        Cd : float
           Drag coefficient of the Decoupler.

        Notes
        -----
        """
        Part.__init__(self, name, m, cost, Cd)
      
class Stage(Part):
    """Subclass of Part object to act as a container of other Parts.

    Methods
    -------
    __init__

    Instance Variables
    ------------------
    parts : list
       List of Part subclass objects specifying the components of the Stage.
    """
    def  __init__(self, parts):
        """Prepare all Stage instance variables.

        Returns
        -------
        None

        Parameters
        ----------
        parts : list
           List of Part subclasses specifying the components of the Stage.

        Notes
        -----
        """
        self.parts = parts
        self.m = 0.0
        for obj in parts:
            self.m += obj.mass

class Rocket:
    """Contains stages and has methods for construction and flying.

    Methods
    -------
    __init__
    assembleStages
    launch
    go

    Instance Variables
    ------------------
    stages : list
       List of Stage objects specifying the components of the Rocket.

    m : float
       Mass of the Rocket.

    x : float
       Current x position of the Rocket.

    y : float
       Current y position of the Rocket.

    z : float
       Current z position of the Rocket.

    vx : float
       Current x component of the Rocket's velocity.

    vy : float
       Current y component of the Rocket's velocity.

    vz : float
       Current z component of the Rocket's velocity.

    ax : float
       Current x component of the Rocket's acceleration.

    ay : float
       Current y component of the Rocket's acceleration.

    az : float
       Current z component of the Rocket's acceleration.

    vx_avg : float
       Current average x component of the Rocket's velocity between two time
       steps.

    vy_avg : float
       Current average y component of the Rocket's velocity between two time
       steps.

    vz_avg : float
       Current average z component of the Rocket's velocity between two time
       steps.

    head : float
       The compass direction the Rocket is facing in radians, ranging from 0 to
       2*pi running clockwise. 0 is facing true north (positive x direction) and
       pi/2 is facing east (positive y direction).

    pitch : float
       The orientation of the rocket relative to horizontal in radians, ranging
       from pi/2 (up; positive z direction) to -pi/2 (down; negative z
       direction).
    """

    def __init__(self, stages):
        """Prepare Rocket instance variables.

        Returns
        -------
        None

        Parameters
        ----------
        stages : list
           List of Stage objects specifying the components of the Rocket.

        Notes
        -----
        Store the constituent stages in the Rocket object and sum up all of the
        mass for each stage to determine the total Rocket mass.
        """
        print "Initialized a Rocket."
        self.stages = stages
        self.m = 0.0
        for eachStage in stages:
            self.m += eachStage.m

    def assembleStages(self):
        """**Place holder right now, needs work.***
        """
        print "Ready to assemble stages!"

    def launch(self, x0, y0, z0, v0x, v0y, v0z, a0x, a0y, a0z, head0, pitch0):
        """Initialize the position and motion variables of the Rocket.

        Returns
        -------
        None

        Parameters
        ----------
        x0 : float
           Initial x position of the Rocket.

        y0 : float
           Initial y position of the Rocket.

        z0 : float
           Initial z position of the Rocket.

        v0x : float
           Initial x component of the Rocket's velocity.

        v0y : float
           Initial y component of the Rocket's velocity.

        v0z : float
           Initial z component of the Rocket's velocity.

        a0x : float
           Initial x component of the Rocket's acceleration.

        a0y : float
           Initial y component of the Rocket's acceleration.

        a0z : float
           Initial z component of the Rocket's acceleration.

        head0 : float
           Initial compass direction the Rocket is pointing, in radians.

        pitch0 : float
           Initial direction the Rocket is pointing relative to horizontal, in
           radians.

        Notes
        -----
        """
        self.x = x0
        self.y = y0
        self.z = z0
        self.vx = v0x
        self.vy = v0y
        self.vz = v0z
        self.ax = a0x
        self.ay = a0y
        self.az = a0z
        self.head = head0
        self.pitch = pitch0

    def go(self, x, y, z, dt):
        """Compute rocket position and velocity after a given timestep.

        Returns
        -------
        None

        Parameters
        ----------
        x : float
           Rocket x position.

        y : float
           Rocket y position.

        z : float
           Rocket z position.

        dt : float
           Time step to advance by in seconds.

        Notes
        -----
        It seems like x, y and z keywords are not used so they can be removed.
        It would seem an positional information would just be retrieved from the
        Rocket object itself so there shouldn't be any need to input positions.
        nbrunett could be misinterpreting something however...
        """
        #add acc. due to Engine thrust
        totAx = 0.0
        totAy = 0.0
        totAz = 0.0
        for stage in self.stages:
            for part in stage.parts:
                if part.__class__.__name__ == 'Engine':
                    totAx += (part.FvsT(part.delT)/self.m)*\
                             math.sin(abs(self.pitch-(math.pi/2.0)))*\
                             math.cos(self.head)
                    totAy += (part.FvsT(part.delT)/self.m)*\
                             math.sin(abs(self.pitch-(math.pi/2.0)))*\
                             math.sin(self.head)
                    totAz += (part.FvsT(part.delT)/self.m)*\
                             math.cos(abs(self.pitch-(math.pi/2.0)))
        #add acc. initialized to Rocket (e.g. gravity)
        totAx += self.ax
        totAy += self.ay
        totAz += self.az
        
        halfdt = dt/2.0
        #Advance 1/2 tstep to find avg v and new acc.
        self.vx_avg = self.vx + totAx*halfdt
        self.vy_avg = self.vy + totAy*halfdt
        self.vz_avg = self.vz + totAz*halfdt
        #Put acc. calculation here
        self.x += self.vx_avg*dt
        self.y += self.vy_avg*dt
        self.z += self.vz_avg*dt
        self.vx += totAx*dt
        self.vy += totAy*dt
        self.vz += totAz*dt

        #increment Engine burn times
        for stage in self.stages:
            for part in stage.parts:
                if part.__class__.__name__ == 'Engine':
                    part.delT += dt
