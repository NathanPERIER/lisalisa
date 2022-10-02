package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;
import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lat.elpainauchoco.lisalisa.data.user.CharacterConf;
import lat.elpainauchoco.lisalisa.data.user.PityConf;
import lat.elpainauchoco.lisalisa.data.user.UserConf;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

@Component
public class UserConfSanitiser {

    private static final Pattern USER_ID_REG = Pattern.compile("[1-9][0-9]{8}");
    private static final Pattern USER_NAME_REG = Pattern.compile("[^\\n\\t\\r]+");

    private final GameDataService gservice;

    @Autowired
    public UserConfSanitiser(final GameDataService gs) {
        gservice = gs;
    }

    public void sanitiseUser(final UserConf user) {
        sanitiseUserId(user.getId());
        sanitiseUserName(user.getName());
        // TODO description
        sanitiseWorldLevel(user.getWorldLevel());
        sanitiseAdventureRank(user.getAdventureRank(), user.getWorldLevel());
        sanitiseProfileCharacter(user.getProfile(), user.getCharacters());
        sanitisePity(user.getPity());
        // TODO limit
        sanitiseCharacters(user);
    }

    protected void sanitiseUserId(final String uid) {
        if(!USER_ID_REG.matcher(uid).matches()) {
            throw new UserConfigException("Bad user id format");
        }
    }

    protected void sanitiseUserName(final String username) {
        if(!USER_NAME_REG.matcher(username).matches()) {
            throw new UserConfigException("Bad username");
        }
    }

    protected void sanitiseWorldLevel(final int wl) {
        if(wl < gservice.getMinWL() || wl > gservice.getMaxWL()) {
            throw new UserConfigException("Bad world level " + wl);
        }
    }

    protected void sanitiseAdventureRank(final int ar, final int wl) {
        if(ar < gservice.getMinAR(wl) || ar > gservice.getMaxAR(wl)) {
            throw new UserConfigException("Bad adventure rank " + ar + " at world level " + wl);
        }
    }

    protected void sanitiseProfileCharacter(final String profile, final Map<String, CharacterConf> characters) {
        if(!characters.containsKey(profile)) {
            throw new UserConfigException("Profile character has to be owned by the user");
        }
    }

    protected void sanitisePity(final PityConf pity) {
        if(pity == null) {
            throw new UserConfigException("Pity configuration cannot be null");
        }
        if(pity.getPerma() < gservice.getMinPity() || pity.getPerma() > gservice.getMaxPity()) {
            throw new UserConfigException("Invalid pity value " + pity.getPerma() + " on the permanent banner");
        }
        if(pity.getTempo() < gservice.getMinPity() || pity.getTempo() > gservice.getMaxPity()) {
            throw new UserConfigException("Invalid pity value " + pity.getTempo() + " on the temporary banner");
        }
    }

    protected void sanitiseCharacters(final UserConf user) {
        if(user.getCharacters() == null) {
            throw new UserConfigException("Character configuration cannot be null");
        }
        if(user.getCharacters().size() == 0) {
            throw new UserConfigException("User has to have at least one character");
        }
        List<CharacterConfSanitiser> charSanitisers = user.getCharacters().keySet().stream()
                .map(char_id -> new CharacterConfSanitiser(gservice, char_id, user))
                .collect(Collectors.toList());
        // If this passes, then all the IDs are correct
        // We then need to check that there is at least one traveler
        List<String> traveler_ids = user.getCharacters().keySet().stream()
                .filter(char_id -> char_id.startsWith("traveler"))
                .collect(Collectors.toList());
        if(traveler_ids.isEmpty()) {
            throw new UserConfigException("User has to have at least one traveler");
        }
        // We also need to check that there is no girl/boy mix
        final long nb_boys = traveler_ids.stream().filter(user_id -> user_id.startsWith("traveler_boy_")).count();
        if(nb_boys != 0) {
            final long nb_girls = traveler_ids.stream().filter(user_id -> user_id.startsWith("traveler_girl_")).count();
            if(nb_girls != 0) {
                throw new UserConfigException("User cannot have both boy travelers and girl travelers");
            }
        }
        charSanitisers.forEach(CharacterConfSanitiser::sanitise);
    }

}
