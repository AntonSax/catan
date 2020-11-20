General idea is to recreate the game of Catan.

Most board games take place on a linear path or a euclidean grid.
Catan takes place in a 2D world, but uses a hexagonal grid.

While a 2-dimensional data structure could work for to represent the layout
  of Catan, it seems (after reading a StackOverflow page on it) more efficient
  to represent the game board in a 3-dimensional data structure to represent
  the hexagonal board. Each dimension: x, y, and z, represent an axis
  on the board in a positive or negative direction, where the axis passes
  through two line segments opposite of each other and the center of each
  hexagon piece. You can also visualize it as only being able to move forward
  or backward on the board, and rotating switches the dimension you move in.

                             ___________
                            /     y     \
                           /           x \
                          /               \
                          \            z  /
                           \             /
                            \___________/


                             ___________
                            /     +y    \
                           / -z       +x \
                          /               \
                          \  -x        +z /
                           \      -y     /
                            \___________/


This means that if we move one space in any direction, we will need to
  update all three of the coordinates. With Catan, we place pieces not only on
  the center of each space, but also on its corners and edges. This alignment
  of the axes this way should allow a better design for representation of
  pieces there.

For each 'Board Coordinate' it shall have a variety of attributes to represent
  whether it is piece, edge, or corner









                 -----   USEFUL RESOURCES   -----
--------------------------------------------------------------------
https://www.redblobgames.com/grids/hexagons/
https://www.catan.com/service/game-rules
http://www-cs-students.stanford.edu/~amitp/game-programming/grids/
https://jonzia.github.io/Catan/
https://gist.github.com/sareon/1365808
