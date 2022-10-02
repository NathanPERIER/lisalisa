package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;
import lat.elpainauchoco.lisalisa.data.game.CharacterData;
import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lat.elpainauchoco.lisalisa.data.user.CharacterAscensionLimit;
import lat.elpainauchoco.lisalisa.data.user.CharacterConf;
import lat.elpainauchoco.lisalisa.data.user.UserConf;

public class CharacterConfSanitiser {

    private final GameDataService gservice;
    private final String char_id;
    private final UserConf user;
    private final CharacterConf character;
    private final CharacterData data;

    public CharacterConfSanitiser(final GameDataService gservice, final String char_id, final UserConf user) {
        this.gservice = gservice;
        this.char_id = char_id;
        if(!gservice.hasCharacter(char_id)) {
            throw new UserConfigException("Character " + char_id + " does not exist");
        }
        this.user = user;
        this.character = user.getCharacters().get(char_id);
        if(character == null) {
            throw new UserConfigException("Configuration for character " + char_id + " cannot be null");
        }
        this.data = gservice.getCharacter(char_id);
    }

    public void sanitise() {
        sanitiseCharacterAscension(character.getAscension(), user.getAdventureRank());
        sanitiseCharacterLevel(character.getLevel(), character.getAscension());
        sanitiseCharacterConstellations(character.getConstellations());
        sanitiseCharacterTalent(character.getNormalAttack(), "normal attack", character.getAscension());
        sanitiseCharacterTalent(character.getElementalSkill(), "elemental skill", character.getAscension());
        sanitiseCharacterTalent(character.getElementalBurst(), "elemental burst", character.getAscension());
        sanitiseCharacterLimits(character.getLimit());
        // TODO weapon
        // TODO artifacts
        // TODO glider
        sanitiseCharacterSkin(character.getSkin());
    }

    public void sanitiseCharacterAscension(final int ascension, final int ar) {
        if(ascension < gservice.getMinAscension()) {
            throw new UserConfigException("Invalid character ascension " + ascension
                    + " for character " + char_id
            );
        }
        if(ascension > gservice.getMaxAscension(ar)) {
            throw new UserConfigException("Invalid character ascension " + ascension
                    + " at adventure rank " + ar
                    + " for character " + char_id
            );
        }
    }

    public void sanitiseCharacterLevel(final int level, final int ascension) {
        if(level < gservice.getMinLevel(ascension) || level > gservice.getMaxLevel(ascension)) {
            throw new UserConfigException("Invalid character level " + level
                    + " at ascension " + ascension
                    + " for character " + char_id
            );
        }
    }

    public void sanitiseCharacterConstellations(final int constellations) {
        if(constellations < gservice.getMaxConstellations() || constellations > gservice.getMaxConstellations()) {
            throw new UserConfigException("Invalid number of constellations for character " + char_id);
        }
    }

    public void sanitiseCharacterTalent(final int talentLevel, final String talentType, final int ascension) {
        if(talentLevel < gservice.getMinTalent()) {
            throw new UserConfigException("Invalid " + talentType + " level " + talentLevel
                    + " for character " + char_id
            );
        }
        if(talentLevel > gservice.getMaxTalent(ascension)) {
            throw new UserConfigException("Invalid " + talentType + " level " + talentLevel
                    + " at ascension " + ascension
                    + " for character " + char_id
            );
        }
    }

    protected void sanitiseCharacterLimits(final CharacterAscensionLimit limits) {
        if(limits == null) {
            return;
        }
        int ascension = limits.getAscension();
        if(ascension < gservice.getMinAscension() || ascension > gservice.getMaxAscension()) {
            throw new UserConfigException("Invalid ascension level " + ascension + " in the limits of character " + char_id);
        }
        int level = limits.getLevel();
        if(level < gservice.getMinLevel(ascension) || level > gservice.getMaxLevel(ascension)) {
            throw new UserConfigException("Invalid character level " + level
                    + " with ascension " + ascension
                    + " in the limits of character " + char_id
            );
        }
        sanitiseCharacterTalentLimit(limits.getNormalAttack(), "normal attack", ascension);
        sanitiseCharacterTalentLimit(limits.getElementalSkill(), "elemental skill", ascension);
        sanitiseCharacterTalentLimit(limits.getElementalBurst(), "elemental burst", ascension);
    }

    protected void sanitiseCharacterTalentLimit(final int talentLevel, final String talentType, final int ascension) {
        if(talentLevel < gservice.getMinTalent() || talentLevel > gservice.getMaxTalent(ascension)) {
            throw new UserConfigException("Invalid " + talentType + " level " + talentLevel
                    + " with ascension " + ascension
                    + " in the limits of character " + char_id
            );
        }
    }



    protected void sanitiseCharacterSkin(final String skin) {
        if("default".equals(skin)) {
            return;
        }
        if(!data.getAlternateSkins().contains(skin)) {
            throw new UserConfigException("Skin " + skin + " does not exist for character " + char_id);
        }
    }

}
