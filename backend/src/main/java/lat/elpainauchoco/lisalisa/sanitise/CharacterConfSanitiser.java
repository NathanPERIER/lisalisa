package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;
import lat.elpainauchoco.lisalisa.data.game.CharacterData;
import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lat.elpainauchoco.lisalisa.data.user.CharacterAscensionLimit;
import lat.elpainauchoco.lisalisa.data.user.CharacterConf;
import lat.elpainauchoco.lisalisa.data.user.UserConf;

public class CharacterConfSanitiser {

    private final GameDataService gservice;

    public CharacterConfSanitiser(final GameDataService gs) {
        gservice = gs;
    }

    public void sanitiseCharacter(final String char_id, final CharacterConf character, final UserConf user) {
        if(!gservice.hasCharacter(char_id)) {
            throw new UserConfigException("Character " + char_id + " does not exist");
        }
        if(character == null) {
            throw new UserConfigException("Configuration for character " + char_id + " cannot be null");
        }
        CharacterData charData = gservice.getCharacter(char_id);
        sanitiseCharacterAscension(char_id, character.getAscension(), user.getAdventureRank());
        sanitiseCharacterLevel(char_id, character.getLevel(), character.getAscension());
        sanitiseCharacterConstellations(char_id, character.getConstellations());
        sanitiseCharacterTalent(char_id, character.getNormalAttack(), "normal attack", character.getAscension());
        sanitiseCharacterTalent(char_id, character.getElementalSkill(), "elemental skill", character.getAscension());
        sanitiseCharacterTalent(char_id, character.getElementalBurst(), "elemental burst", character.getAscension());
        sanitiseCharacterLimits(char_id, character.getLimit());
        // TODO weapon
        // TODO artifacts
        // TODO glider
        sanitiseCharacterSkin(char_id, character.getSkin(), charData);
    }

    public void sanitiseCharacterAscension(final String char_id, final int ascension, final int ar) {
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

    public void sanitiseCharacterLevel(final String char_id, final int level, final int ascension) {
        if(level < gservice.getMinLevel(ascension) || level > gservice.getMaxLevel(ascension)) {
            throw new UserConfigException("Invalid character level " + level
                    + " at ascension " + ascension
                    + " for character " + char_id
            );
        }
    }

    public void sanitiseCharacterConstellations(final String char_id, final int constellations) {
        if(constellations < gservice.getMaxConstellations() || constellations > gservice.getMaxConstellations()) {
            throw new UserConfigException("Invalid number of constellations for character " + char_id);
        }
    }

    public void sanitiseCharacterTalent(final String char_id, final int talentLevel, final String talentType,
                                        final int ascension) {
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

    protected void sanitiseCharacterLimits(final String char_id, final CharacterAscensionLimit limits) {
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
        sanitiseCharacterTalentLimit(char_id, limits.getNormalAttack(), "normal attack", ascension);
        sanitiseCharacterTalentLimit(char_id, limits.getElementalSkill(), "elemental skill", ascension);
        sanitiseCharacterTalentLimit(char_id, limits.getElementalBurst(), "elemental burst", ascension);
    }

    protected void sanitiseCharacterTalentLimit(final String char_id, final int talentLevel, final String talentType,
                                                final int ascension) {
        if(talentLevel < gservice.getMinTalent() || talentLevel > gservice.getMaxTalent(ascension)) {
            throw new UserConfigException("Invalid " + talentType + " level " + talentLevel
                    + " with ascension " + ascension
                    + " in the limits of character " + char_id
            );
        }
    }



    protected void sanitiseCharacterSkin(final String char_id, final String skin, final CharacterData charData) {
        if("default".equals(skin)) {
            return;
        }
        if(!charData.getAlternateSkins().contains(skin)) {
            throw new UserConfigException("Skin " + skin + " does not exist for character " + char_id);
        }
    }

}
