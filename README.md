# magic-hex
Solving the magic hexagon puzzle with brute force.

A magic hexagon is a hexagon of smaller hexagons, wherein each row and column in every direction (3 total directions) adds up to the same number. The classic magic hexagon has 19 cells, and each row must add up to 38. I couldn't solve the physical wooden puzzle I owned, so I wrote this program to do it. It sometimes takes a decent amount of time to run, but it will check most of the combinations (just the ones needed; not all - there are way too many) and output the correct configuration. 

For the other incorrect configurations it tries it will print False (just so you know it's running). I also plan to clean this code up so it's clearer what's going on.

The output is a list of tuple. The first tuple is column 1 of the solution, the rest of the tuples are the rows of the solution from the bottom up.
