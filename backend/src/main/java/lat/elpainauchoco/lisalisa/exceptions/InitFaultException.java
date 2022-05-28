package lat.elpainauchoco.lisalisa.exceptions;

/**
 * Exception used to notify of a problem during the initialisation of the API
 */
public class InitFaultException extends RuntimeException {

    public InitFaultException(final String message) {
        super(message);
    }

    public InitFaultException(final String message, final Throwable t) {
        super(message, t);
    }

}
