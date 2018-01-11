import Grid as bG
import Species as bSp


class Initialization:
    """Framework for Input of Simulation Parameters

    Attributes:
        __s (:obj:Species):
            Contains all Specimen Parameters
        __t (:obj:Grid):
            Contains all Time Parameters
        __p (:obj:Grid):
            Contains all Positional Space Parameters
        __v (:obj:Grid):
            Contains all Velocity Space Parameters
    """
    def __init__(self):
        self.__s = bSp.Species()
        self.__p = bG.Grid()
        self.__t = bG.Grid()
        self.__v = bG.Grid()

    def time(self,
             max_time,
             step_size=None,
             number_time_steps=None):
        self.__t = bGrid.Grid(1,
                              [0.0, max_time],
                              d=step_size,
                              n=number_time_steps,
                              shape='rectangular')

    def position_space(self,
                       dimension,
                       boundaries,
                       step_size=None,
                       total_grid_points=None,
                       shape='rectangular'):
        self.__p = bGrid.Grid(dimension,
                              boundaries,
                              d=step_size,
                              n=total_grid_points,
                              shape=shape)

    def velocity_space(self,
                       dimension,
                       max_v,
                       step_size=None,
                       total_grid_points=None,
                       offset=None,
                       shape='rectangular'):
        if offset is None:
            offset = [0.0]*dimension

        assert type(offset) is list
        assert type(max_v) in [float, int] and max_v > 0
        assert type(single_grid_for_all_specimen) is bool

        boundaries = [[-max_v + offset[i_d], max_v + offset[i_d]]
                      for i_d in range(dimension)]
        self.__v = bGrid.Grid(dimension,
                              boundaries,
                              d=step_size,
                              n=total_grid_points,
                              shape=shape)

    def add_specimen(self,
                     mass=1,
                     alpha_list=None,
                     name=None,
                     color=None):
        self.__s.add_specimen(mass, alpha_list, name, color)

    def print(self):
        print("Specimen:")
        self.__s.print()
        print("Time Grid:")
        self.__t.print()
        print("Positional Grid:")
        self.__p.print()
        print("Velocity Grid:")
        self.__v.print()
