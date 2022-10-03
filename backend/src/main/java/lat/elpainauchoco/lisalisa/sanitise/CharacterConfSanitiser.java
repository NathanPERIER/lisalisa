package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.data.user.*;
import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;
import lat.elpainauchoco.lisalisa.data.game.CharacterData;
import lat.elpainauchoco.lisalisa.data.game.GameDataService;

import java.util.Map;

public class CharacterConfSanitiser extends AscendableSanitiser {

    private final String char_id;
    private final CharacterConf character;
    private final CharacterData data;

    public CharacterConfSanitiser(final GameDataService gservice, final String char_id, final UserConf user) {
        super(gservice, user, "character", char_id);
        if(!gservice.hasCharacter(char_id)) {
            throw new UserConfigException("Character " + char_id + " does not exist");
        }
        this.char_id = char_id;
        this.character = user.getCharacters().get(char_id);
        if(character == null) {
            throw new UserConfigException("Configuration for character " + char_id + " cannot be null");
        }
        this.data = gservice.getCharacter(char_id);
    }

    public void sanitise() {
        sanitiseAscendable(character);
        sanitiseCharacterConstellations(character.getConstellations());
        sanitiseCharacterTalent(character.getNormalAttack(), "normal attack", character.getAscension());
        sanitiseCharacterTalent(character.getElementalSkill(), "elemental skill", character.getAscension());
        sanitiseCharacterTalent(character.getElementalBurst(), "elemental burst", character.getAscension());
        sanitiseCharacterLimits(character.getLimit());
        sanitiseCharacterWeapon(character.getWeapon(), data.getWeapon());
        sanitiseCharacterArtifacts(character.getArtifacts());
        sanitiseCharacterSkin(character.getSkin());
        sanitiseGlider(character.getGlider());
    }

    public void sanitiseCharacterConstellations(final int constellations) {
        if(constellations < gservice.getMinConstellations() || constellations > gservice.getMaxConstellations()) {
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
        sanitiseLimits(limits);
        sanitiseCharacterTalentLimit(limits.getNormalAttack(), "normal attack", character.getAscension());
        sanitiseCharacterTalentLimit(limits.getElementalSkill(), "elemental skill", character.getAscension());
        sanitiseCharacterTalentLimit(limits.getElementalBurst(), "elemental burst", character.getAscension());
    }

    protected void sanitiseCharacterTalentLimit(final int talentLevel, final String talentType, final int ascension) {
        if(talentLevel < gservice.getMinTalent() || talentLevel > gservice.getMaxTalent(ascension)) {
            throw new UserConfigException("Invalid " + talentType + " level " + talentLevel
                    + " with ascension " + ascension
                    + " in the limits of character " + char_id
            );
        }
    }

    protected void sanitiseCharacterWeapon(final WeaponConf weapon, final String weaponType) {
        if(weapon == null) {
            throw new UserConfigException("Configuration for weapon of character " + char_id + " cannot be null");
        }
        final String weaponUid = char_id + "#" + weapon.getId();
        WeaponConfSanitiser sanitiser = new WeaponConfSanitiser(gservice, weapon, weaponUid, user, weaponType);
        sanitiser.sanitise();
    }

    protected void sanitiseCharacterArtifacts(final ArtifactsConf artifacts) {
        if(artifacts == null) {
            throw new UserConfigException("Configuration for artifacts of character " + char_id + " cannot be null");
        }
        for(Map.Entry<String, ArtifactsConf.ArtifactPieceConf> e : artifacts.toMapping().entrySet()) {
            if(e.getValue() != null) {
                String pieceId = char_id + "#" + e.getKey();
                ArtifactConfSanitiser sanitiser = new ArtifactConfSanitiser(gservice, e.getValue(), e.getKey(), pieceId);
                sanitiser.sanitise();
            }
        }
    }

    protected void sanitiseGlider(final String glider) {
        if(!gservice.getGliders().contains(glider)) {
            throw new UserConfigException("Glider " + glider + " equipped by character " + char_id + " does not exist");
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
