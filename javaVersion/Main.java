package levels;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Welcome to my mine game!\n" +
                "Please enter a player name: ");
        String playerName = input.nextLine();
        Player player = new Player(20, playerName);
        System.out.print("Welcome, " + playerName + "!\n" +
                "How many columns would you like the mine to have? Enter an integer greater than 3: ");
        int cols = 0;
        while(cols < 4){
            try{
                cols = input.nextInt();
                if (cols < 4){
                    System.out.print("Sorry, that's 3 or less. Please try again: ");
                    input.nextLine();
                }
            } catch (InputMismatchException e){
                System.out.print("Whoops! That's not an integer. Please try again: ");
                cols = 0;
                input.nextLine();
            }}
        System.out.print("How many rows would you like the mine to have? Enter an integer greater than 3: ");
        int rows = 0;
        while(rows < 4){
            try{
                rows = input.nextInt();
                if (rows < 4){
                    System.out.print("Sorry, that's 3 or less. Please try again: ");
                }
            } catch (InputMismatchException e){
                System.out.print("Whoops! That's not an integer. Please try again: ");
                rows = 0;
                input.nextLine();
            }}
        Mine myMine = new Mine(cols, rows);
        input.nextLine();
        System.out.print("Great! Would you like an explanation on how the game works?\n" +
                "Please enter 'help' or 'no': ");
        String ans = input.nextLine();
        while(!(ans.equals("help") || ans.equals("no"))){
            System.out.print("Sorry, I didn't get that.\n" +
                    "Please enter 'help' or 'no': ");
            ans = input.nextLine();}
        if(ans.equals("help")){
            System.out.println();
            System.out.println("This is a very simple mining game.\n" +
                    "Every turn, you will be able to see the entire mine.\n" +
                    "If a block contains 'T', it means you can reach it - and hit it.\n" +
                    "If a block contains '$', it contains gold, which is what you're after.\n" +
                    "It a block contains '^', it contains a pickaxe, which will add to the amount of hits you have.\n" +
                    "If a block contains 'X', it's dirt and has nothing of value.\n" +
                            "To hit a cell, enter its position using the letter of the column and the number of the row.\n" +
                    "Once you reach 0 hits on the pickaxe, the game ends and it will show you your score.\n");
        }
        int cont = 0;
        while(cont == 0 && player.hits != 0){
            System.out.println("Current stats:");
            System.out.println(player);
            System.out.print("\n \n");
            System.out.println(myMine);
            System.out.print("\n" + "Would you like to hit a cell or exit? \n" +
                    "Press 0 to hit, 1 to exit: ");
            cont = input.nextInt();
            if(cont == 0){
                try {
                    myMine = player.hitCell(myMine);
                } catch (cellNotAttException e) {
                    System.out.println("Ooops!! You cannot hit this cell.");
                } catch (emptyCellException e){
                    System.out.println("Ooops!! That's an empty cell.");}}}
        if(player.hits == 0){
            System.out.println("Game over! Stats: ");
            System.out.print(player);
        }
        System.out.print("Thanks for playing my game!");
    }
}