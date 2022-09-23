##
## EPITECH PROJECT, 2020
## 206neutrinos [WSL: Ubuntu]
## File description:
## Makefile
##

SRC	=	main.py

NAME	=	209poll

all:	$(NAME)

$(NAME):
	@cp $(SRC) $(NAME)
	chmod 755 $(NAME)

clean:
	@echo "done"

fclean:	clean
	@rm -f $(NAME)
	@rm -f data

re:	fclean	all