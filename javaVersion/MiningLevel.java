package levels;

/**
 * A mining level is a collection of Mining Cells that are all at the same height.
 */
public class MiningLevel {
    MiningCell [] cells;

    /**
     * index within Mine's levels.
     */
    int pos;
    int width;
    Mine mine;

    /** Constructor. Calls within it the Mining Cell constructor.
     * @param pos position within the mine
     * @param width width of the mine, i.e. number of cells the Mining Level contains
     * @param mine the Mine the Mining Level is part of
     */
    public MiningLevel(int pos, int width, Mine mine) {
        this.mine = mine;
        this.pos = pos;
        this.width = width;
        this.cells = new MiningCell[width];
        for (int i = 0; i < this.width; i ++){
            this.cells[i] = new MiningCell(this,i, mine.rand);}}

    /** Constructor for head level;
     * @param width width of the mine, i.e. number of cells the Mining Level contains
     */
    public MiningLevel(int width) {
        this.width = width;
        this.pos = -1;
        MiningCell [] celss = new MiningCell[width];
        for(int i= 0; i < width; i++){
            celss[i] = new MiningCell(true, this,i);}
        this.cells = celss;
    }

    /** Displays Mining Level. Calls the toString method of each Mining Cell
     * @return display of the Mining Level
     */
    @Override
    public String toString() {
        String str = "";
        if(this.cells != null){
        for(MiningCell cell : this.cells){
            str += cell.toString();}}
        return str;
    }
}