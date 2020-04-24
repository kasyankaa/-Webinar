from multimethod import multimethod
import doctest


class WithStaticAndOverload:

    worker_name = "Worker"

    @staticmethod
    def do_work():
        pass

    def sing_a_song(self):
        print(WithStaticAndOverload.do_work())

    @multimethod
    def print_data(self, first, second):
        print(str(first) + str(second))

    @multimethod
    def print_data(self, first, second):
        print(str(first + second))

    @multimethod
    def print_data( first: int, second: int):
        """
        returns sum of two integers
        >>> creat_tuple(10, 20)
        (10,30)
        >>>create_tuple(20,70)
        (20,70)
        """
        return (first + second)

    def create_tuple(first: int, second: int):
        """
        returns sum of two integers
        >>> create_tuple(10, 20)
        (10, 20)
        >>> create_tuple(20, 70)
        (20, 70)
        """
        return (first, second)


doctest.testmod(verbose=True)


#if __name__ == '__main__':
  #  my_object = WithStaticAndOverload()
   # my_object.print_data(23, 45)
   # doctest.testmod()
