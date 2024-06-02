package levels;

import java.util.ArrayList;
import java.util.Random;

public class Mine {
    MiningLevel head;
    MiningLevel bottom;
    MiningLevel [] levels;
    int height;
    int width;
    Random rand;

    /**
     * Constructor
     * @param height how many rows the mine has
     * @param width how many columns the mine has
     */
    public Mine(int height, int width) {
        this.rand = new Random();
        this.rand.setSeed(47);
        this.width = width;
        this.height = height;
        this.head = new MiningLevel(width);
        this.levels = new MiningLevel[height];
        for(int m = 0; m<height;m++){
            this.levels[m] = new MiningLevel(m,width,this);}
        this.bottom = new MiningLevel(height,width,this);
        ArrayList<MiningCell> atta = new ArrayList<>();
        for(int k = 0; k < this.levels[0].cells.length; k++){
            this.levels[0].cells[k].attainable = true;
            if(this.levels[0].cells[k].type.equals("empty")){
                atta.add(this.levels[0].cells[k]);}}
        this.setAttainable(atta);
        this.head.mine = this;
    }

    /**
     * Adds a new level of the mine
     * @param hitCell Mining Cell that the user hit
     * @param att ArrayList of reachable cells
     * @return updated ArrayList of reachable cells
     */
    public ArrayList<MiningCell> addLevel(MiningCell hitCell, ArrayList<MiningCell> att){
        this.head = this.levels[0];
        this.head.pos = -1;
        MiningLevel [] newLvls = new MiningLevel[this.height];
        for(int l = 0; l < this.height -1; l++){
            newLvls[l] = this.levels[l+1];
            newLvls[l].pos--;}
        newLvls[this.height -1] = this.bottom;
        newLvls[this.height -1].pos--;
        this.levels = newLvls;
        this.bottom = new MiningLevel(this.height,this.width,this);
        this.bottom.cells[hitCell.pos].attainable = true;
        if(this.bottom.cells[hitCell.pos].type.equals("empty")){
        att.add(this.bottom.cells[hitCell.pos]);}
        return att;}

    /**
     * Finds which cells the player can reach, and sets them as reachable
     * @param att ArrayList of attainable cells. Initially will contain only the
     *            block that the user has hit.
     */
    public void setAttainable(ArrayList<MiningCell> att){
        for(int j = 0; j<att.size(); j++){
            int x = att.get(j).pos;
            int y = att.get(j).miningLevel.pos;
            //set bottom:
            if(y < (height -1)){
                if(!this.levels[y+1].cells[x].attainable){
                    this.levels[y+1].cells[x].attainable = true;
                    if(this.levels[y+1].cells[x].type.equals("empty") && !(att.contains(this.levels[y+1].cells[x]))){
                        att.add(this.levels[y+1].cells[x]);}}
            } else if(y == (height-1)) {
                if(!this.bottom.cells[x].attainable) {
                    this.bottom.cells[x].attainable = true;
                    if (this.bottom.cells[x].type.equals("empty")) {
                        att = this.addLevel(att.get(j), att);
                        y--;
                    }
                }
            } else {
                att = this.addLevel(att.get(j), att);
                y--;
            }
            //set top cell to attainable:
            if(y != 0){
                if(!this.levels[y-1].cells[x].attainable) {
                    this.levels[y - 1].cells[x].attainable = true;
                    if (this.levels[y - 1].cells[x].type.equals("empty") && !(att.contains(this.levels[y - 1].cells[x]))) {
                        att.add(this.levels[y - 1].cells[x]);
                    }
                }}
            //set left:
            if(x != 0){
                //if(y!=this.height) {
                    if (!this.levels[y].cells[x - 1].attainable) {
                        this.levels[y].cells[x - 1].attainable = true;
                        if (this.levels[y].cells[x - 1].type.equals("empty") && !(att.contains(this.levels[y].cells[x - 1]))) {
                            att.add(this.levels[y].cells[x - 1]);}}
            }
            //set right:
            if(x != (width -1)){
                //if(y != this.height) {
                    if (!this.levels[y].cells[x + 1].attainable) {
                        this.levels[y].cells[x + 1].attainable = true;
                        if (this.levels[y].cells[x + 1].type.equals("empty") && !(att.contains(this.levels[y].cells[x + 1]))) {
                            att.add(this.levels[y].cells[x + 1]);}}
            }}
    }

    /** Displays mine
     * @return mine in text format
     */
    @Override
    public String toString() {
        String str = "";
        char c = 'A';
        for(int i = 0; i < this.width; i++){
            str += "  " + c + " ";
            c++;}
        str += "\n";
        str += this.head.toString();
        str += "\n";
        String separator = "";
        for(int i = 0; i < this.width; i++){
            separator += "----";}
        separator += "\n";
        str += separator + separator;
        int jj = 0;
        for(MiningLevel lvl : this.levels){
            str += lvl.toString();
            str += jj++;
            str += "\n" + separator;}
        str += separator;
        str += this.bottom.toString();
        return str;
    }
}
