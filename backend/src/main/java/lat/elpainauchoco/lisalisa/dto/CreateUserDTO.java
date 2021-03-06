package lat.elpainauchoco.lisalisa.dto;

import lat.elpainauchoco.lisalisa.gamedata.GameDataService;
import lat.elpainauchoco.lisalisa.userdata.UserConf;
import lombok.Setter;

@Setter
public class CreateUserDTO {

    private String password;
    private String name;
    private UserConf.TravelerType traveler;

    public UserConf createUserConf(final String id, final GameDataService gdata) {
        return new UserConf(id, name, traveler, gdata);
    }

}
