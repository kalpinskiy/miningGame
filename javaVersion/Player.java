package levels;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Player class. Allows the creating of a player for the game and keeps track of the player's attributes.
 */
public class Player {
    int gold;
    int hits;
    String name;

    /**
     * Constructor for the player class.
     * @param hits how many hits the player starts with
     * @param name player name
     */
    public Player(int hits, String name) {
        this.hits = hits;
        this.gold = 0;
        this.name = name;}

    /**
     * Allows the player to hit a cell.
     * @param mine Mine in which action is taking place
     * @return updated Mine
     * @throws cellNotAttException if it's impossible to reach the cell the user wants to hit
     * @throws emptyCellException if the cell the user wants to hit is empty
     */
    public Mine hitCell(Mine mine) throws cellNotAttException, emptyCellException {
        Scanner input2 = new Scanner(System.in);
        System.out.print("Please enter column letter: ");
        char lett = input2.next().charAt(0);
        int coll = lett - 'A';
        System.out.print("Please enter the number of the row: ");
        int roww = input2.nextInt();
        MiningCell cell;
        if(roww == mine.height){
            cell = mine.bottom.cells[coll];
        } else {
            cell = mine.levels[roww].cells[coll];
        }
        if(!cell.attainable){
            throw new cellNotAttException();
        } else {
            if(cell.type == "empty"){
                throw new emptyCellException();}
            if(cell.type == "money"){
                this.gold++;
            } else if (cell.type == "ax") {
                this.hits += 5;}
            this.hits--;
            cell.type = "empty";
            ArrayList<MiningCell> att1 = new ArrayList<>();
            att1.add(cell);
            mine.setAttainable(att1);
        } return mine;}

    /**
     * Shows player attributes.
     * @return Player's information
     */
    @Override
    public String toString() {
        String playerInfo = "Player: " + this.name + "\t Hits left: " + this.hits + "\t Gold: " + this.gold;
        return playerInfo;
    }
}
