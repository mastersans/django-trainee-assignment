from typing import Generic, TypeVar, Generator, Dict


T = TypeVar('T', int, float)

class Rectangle(Generic[T]):
    __width: T
    __height: T

    def __init__(self, width: T, height: T):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self.__width = width
        self.__height = height

    def __iter__(self) -> Generator[Dict[str, int], None, None]:
        yield {'length': self._length}
        yield {'width': self._width}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self._length == other._length and self._width == other._width
    
    def __lt__(self, other: 'Rectangle') -> bool:
        return self.get_area() < other.get_area()
    
    def get_width(self) -> T:
        """Return the width of the rectangle"""
        return self.__width
    
    def get_height(self) -> T:
        """Return the height of the rectangle"""
        return self.__height
    
    def set_width(self, width: T) -> None:
        """Set the width of the rectangle"""
        self.__width = width
    
    def set_height(self, height: T) -> None:
        """Set the height of the rectangle"""
        self.__height = height

    def get_area(self) -> T:
        """Return the area of the rectangle"""
        return self.__width * self.__height
    
    def get_perimeter(self) -> T:
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self._length + self._width)

