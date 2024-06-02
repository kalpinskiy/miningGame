package levels;


import java.util.Random;

/**
 * Basic building block of the game.
 */
public class MiningCell {
    boolean attainable;
    String type;
    /**
     * Not used - meant for future developments that include cells that take various amounts of hits to break.
     */
    int difficulty;
    MiningLevel miningLevel;
    int pos;

    /**
     * Constructor for the basic mining cell.
     * @param miningLevel Mining Level that the cell is part of
     * @param pos position within said Mining Level
     * @param rand Random generator. Passing it from the Mine class allows to set a seed
     *             for the whole mine
     */
    public MiningCell(MiningLevel miningLevel, int pos, Random rand) {
        int randInt = rand.nextInt(10);
        if(randInt < 5){
            this.type = "dirt";
        } else if (randInt < 8){
            this.type = "empty";
        } else if (randInt < 9){
            this.type = "money";
        } else{
            this.type = "ax";}
        this.difficulty = 1;
        this.attainable = false;
        this.miningLevel = miningLevel;
        this.pos = pos;
    }

    /**
     * Constructor for Mine's head's cells - empty, attainable cells
     * @param attainable typically True
     * @param miningLevel Mining Level of which the cell is part of
     * @param pos position within said Mining Level
     */
    public MiningCell(boolean attainable, MiningLevel miningLevel, int pos) {
        this.attainable = attainable;
        this.type = "empty";
        this.miningLevel = miningLevel;
        this.pos = pos;
    }

    /**
     * Displays the cell.
     * @return the cell
     */
    @Override
    public String toString() {
        String str = str = "|";
        if(this.attainable){
            str+= "T";
        } else{
            str += " ";
        }
        switch (this.type){
            case "empty":
                str += " |";
                break;
            case "money":
                str += "$|";
                break;
            case "dirt":
                str += "X|";
                break;
            case "ax":
                str += "^|";
                break;}
        return str;}
}
