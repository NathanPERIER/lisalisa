package lat.elpainauchoco.lisalisa.userdata;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class PityConf {

    private int perma;
    private int tempo;
    private boolean guaranteed;

    public PityConf() {
        perma = 0;
        tempo = 0;
        guaranteed = false;
    }

}
