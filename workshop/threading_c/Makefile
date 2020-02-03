##
## EPITECH PROJECT, 2019
## Makefile
## File description:
## makefile for bistro-matic
##

SRC		=		*.c

SRCT 	=		./tests/

NAME	=		bsq

FLAGS	=		-lpthread -Ofast

TFLAG 	= 		-lcriterion --coverage -fprofile-arcs

COV 	=		--exclude tests/ -o coverage.html



all:
		gcc -o $(NAME) $(SRC) $(FLAGS)

clean:
		rm -f $(OBJ)
		rm -f *.html
		rm -f *.gcno
		rm -f *.gcda

fclean:	clean
		rm -f $(NAME)
		rm -f *.gcno
		rm -f *.gcda
		rm -f *.html
		rm -f vgcore.*

clear:
		clear

re: clear fclean all

tests_run:
		gcc -o $(NAME) $(SRC) $(SRCT) $(TFLAG) $(FLAGS)
		-./$(NAME)
		gcovr --exclude tests/
		gcovr --html $(COV) --html-title $(NAME) --html-details
		rm -f *.gcno
		rm -f *.gcda

vaslgrind: fclean
	clear
	gcc -g -o $(NAME) $(SRC) $(FLAGS)
	valgrind -s --leak-check=full --track-origins=yes ./$(NAME) intermediate_map_500_500_3 #> valgrind_log

#mouli_maps_solved/intermediate_map_200_200_notsolve

#563434*232323%(233424+23423423-23482347)


callgrind3D: fclean
	rm -f callgrind.*
	clear
	gcc -g -O4 -o $(NAME) $(SRC) $(FLAGS)
	valgrind --tool=callgrind ./$(NAME) intermediate_map_10000_10000 #&> valgrind_log
	kcachegrind callgrind.*

profiler:
	gcc -pg -O4 -o $(NAME) $(SRC) $(FLAGS)


time_test:
	gcc -g -o $(NAME) $(SRC) $(FLAGS)
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	gcc -O1 -g -o $(NAME) $(SRC) $(FLAGS)
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	gcc -O2 -g -o $(NAME) $(SRC) $(FLAGS)
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	gcc -O3 -g -o $(NAME) $(SRC) $(FLAGS)
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	gcc -O4 -g -o $(NAME) $(SRC) $(FLAGS)
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
	time ./$(NAME) mouli_maps/intermediate_map_10000_10000 > log
