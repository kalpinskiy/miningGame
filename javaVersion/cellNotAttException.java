package levels;

public class cellNotAttException extends Exception{
    public cellNotAttException() {
        super("can't hit cell");
    }

    public cellNotAttException(String message) {
        super(message);
    }
}
