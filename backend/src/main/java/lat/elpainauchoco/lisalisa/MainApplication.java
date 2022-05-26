package lat.elpainauchoco.lisalisa;

import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.core.LoggerContext;
import org.apache.logging.log4j.core.config.Configuration;
import org.apache.logging.log4j.core.config.LoggerConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MainApplication {

    private static final Logger logger = LogManager.getLogger(MainApplication.class);

    public static void verbose() {
        LoggerContext ctx = (LoggerContext) LogManager.getContext(false);
        Configuration config = ctx.getConfiguration();
        LoggerConfig loggerConfig = config.getLoggerConfig(LogManager.ROOT_LOGGER_NAME);
        loggerConfig.setLevel(Level.ALL);
        ctx.updateLoggers();
        logger.trace("Verbose enabled");
    }

    public static void main(String[] args) {
        if(args.length > 0 && "-v".equals(args[0])) {
            verbose();
        }
        SpringApplication.run(MainApplication.class, args);
    }

}
