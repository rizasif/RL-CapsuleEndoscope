
class Config:
    
    #LABVIEW Configuration
    VI_PATH='C:\\LabView\\Mark2\\Python_Comm\\Python_Comm.vi'

    MASTER_LABEL = ('master_x', 'master_y', 'master_z', 'master_mx', 'master_my', 'master_mz')
    SLAVE_LABEL = ('slave_x', 'slave_y', 'slave_z', 'slave_mx', 'slave_my', 'slave_mz')
    AMP_LABEL = ('a_1','a_2','a_3','a_4','a_5','a_6','a_7','a_8','a_9')
    
    # Orientation Configuration Parameters in millimeters
    X_MAX_VAL = 250.0
    X_MIN_VAL = -250.0
    Y_MAX_VAL = 250.0
    Y_MIN_VAL = -250.0
    Z_MAX_VAL = 250.0
    Z_MIN_VAL = -250.0

    X_MAX_DEVIATE = 20.0
    Y_MAX_DEVIATE = 0.0
    Z_MAX_DEVIATE = 0.0    

    X_MAX_MAG_MOMENT = 7.0
    X_MIN_MAG_MOMENT = -7.0
    Y_MAX_MAG_MOMENT = 7.0
    Y_MIN_MAG_MOMENT = -7.0
    Z_MAX_MAG_MOMENT = 7.0
    Z_MIN_MAG_MOMENT = -7.0

    X_MAX_MAG_MOMENT_DEVIATE = 3.0
    Y_MAX_MAG_MOMENT_DEVIATE = 0.0
    Z_MAX_MAG_MOMENT_DEVIATE = 0.0

    #Probe dimention in mm
    PROBE_DIM = 1
    
    #activate X/Y/Z coordinates OR X/Y/Z M. Moment OR both
    # COORD -> coordinates
    # MOMENT -> M. Moments
    # BOTH -> Both
    # Default -> Both
    TRAINING_MODE = "MOMENT"
    
    #Reward gradient
    REWARD_GRADIENT = 10
    
    # in amperes 
    MAX_CURRENT = 2.0
    MIN_CURRENT = -2.0
    CURR_DEVIATE_ACTIVE = False
    MAX_CURR_DEVIATE = 1.0
    MIN_CURR_DEVIATE = -1.0

    #Change Currents time per second
    RUN_TIMES_PER_SEC = 1

    #Timestep Limit for episode
    TIMESTEP_LIMIT = 5
    RESET_STEP_COUNT = 10

    #LOGFILE name without file extension (.log will be appended to filename)
    LOGFILE = "./log/magroboenv_"

    