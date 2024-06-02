package levels;

public class emptyCellException extends Exception{
    public emptyCellException() {
        super("that's an empty cell");
    }

    public emptyCellException(String message) {
        super(message);
    }

}
