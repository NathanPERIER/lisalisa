package lat.elpainauchoco.lisalisa;

import lat.elpainauchoco.lisalisa.dto.CreateUserDTO;
import lat.elpainauchoco.lisalisa.gamedata.GameDataService;
import lat.elpainauchoco.lisalisa.userdata.UserConf;
import lat.elpainauchoco.lisalisa.userdata.sanitise.UserConfSanitiser;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.lang.model.type.NullType;

@RestController
@RequestMapping("/api")
public class ApiController {

    @Autowired
    private UserConfSanitiser sanitiser;

    @Autowired
    private GameDataService gdata;

    public ApiController() {
        MainApplication.verbose();
    }

    private static final Logger logger = LogManager.getLogger(MainApplication.class);

    @PutMapping("/user/{id}")
    public ResponseEntity<NullType> putUser(@PathVariable(value = "id") final String uid, @RequestBody final CreateUserDTO create) {
        // TODO
        return ResponseEntity.ok().build();
    }

    @PostMapping("/conf/{id}")
    public ResponseEntity<NullType> postConf(@PathVariable(value = "id") final String uid) {
        // TODO
        logger.trace(uid);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/test")
    public ResponseEntity<UserConf> getTest() {
        // TODO
        return ResponseEntity.ok(new UserConf("7000000", "Jean", UserConf.TravelerType.BOY, gdata));
    }

}
