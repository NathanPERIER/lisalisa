package lat.elpainauchoco.lisalisa.exceptions;

/**
 * Exception used to notify of a problem with the user configuration
 */
public class UserConfigException extends RuntimeException {

    public UserConfigException(String message) {
        super(message);
    }

}
