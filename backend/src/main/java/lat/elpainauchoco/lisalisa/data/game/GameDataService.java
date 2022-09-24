package lat.elpainauchoco.lisalisa.data.game;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lat.elpainauchoco.lisalisa.exceptions.InitFaultException;
import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;
import lombok.Getter;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.Map;

@Service
public class GameDataService {

    private static final Logger logger = LogManager.getLogger(GameDataService.class);

    public static final String DEFAULT_CHARACTER_SKIN = "default";

    private final AscensionLevelData[] ascensions;
    private final int[][] world_levels;
    private final List<AdventureRankData> adventure_ranks;
    private final Map<String, CharacterData> characters;

    @Getter
    private final int minWL;
    @Getter
    private final int maxWL;
    @Getter
    private final int minTalent;
    @Getter
    private final int minAscension;
    @Getter
    private final int minConstellations;
    @Getter
    private final int maxConstellations; // TODO move to `CharacterData`
    @Getter
    private final int minRefinement;
    @Getter
    private final int minPity;
    @Getter
    private final int maxPity;
    @Getter
    private final int minArtLevel;
    @Getter
    private final int artifactBasis;


    public GameDataService() {
        // associative array of all the possible characters
        characters = readFromJar("/genshin/characters.json", new TypeReference<>() { });
        // array where the index is the ascension (character or weapon)
        ascensions = readFromJar("/genshin/ascension.json", new TypeReference<>() { });
        // array where the index is the world level, and the values are arrays of two integers (min and max ascension for this wl)
        world_levels = readFromJar("/genshin/world_level.json", new TypeReference<>() { });
        // array of objects that associate a range of ar with a maximum ascension
        adventure_ranks = readFromJar("/genshin/adventure_rank.json", new TypeReference<>() { });
        Map<String, Integer> constants = readFromJar("/genshin/numeric_constants.json", new TypeReference<>() { });
        minWL = constants.get("world.level.min");
        maxWL = minWL + world_levels.length - 1;
        minTalent = constants.get("talent.level.min");
        minAscension = constants.get("ascension.level.min");
        minConstellations = constants.get("constellations.num.min");
        maxConstellations = constants.get("constellations.num.max");
        minRefinement = constants.get("refinement.level.min");
        minPity = constants.get("banner.pity.min");
        maxPity = constants.get("banner.pity.max");
        minArtLevel = constants.get("artifact.level.min");
        artifactBasis = constants.get("artifact.upgrade.basis");
    }

    public int getMinAR(int world_level) {
        return world_levels[world_level][0];
    }

    /** Retrieves the maximum adventure rank at a certain world level */
    public int getMaxAR(int world_level) {
        return world_levels[world_level][1];
    }

    /** Retrieves the maximum adventure rank achievable */
    public int getMaxAR() {
        return getMaxAR(getMaxWL());
    }

    /** Retrieves the maximum ascension level at a certain adventure rank */
    public int getMaxAscension(int adventure_rank) {
        for(AdventureRankData ard : adventure_ranks) {
            if(ard.inRange(adventure_rank)) {
                return ard.getMaxAscension();
            }
        }
        throw new UserConfigException("Bad adventure rank : " + adventure_rank);
    }

    /** Retrieves the maximum ascension level achievable */
    public int getMaxAscension() {
        return getMaxAscension(getMaxAR());
    }

    public int getMinLevel(int ascension) {
        return ascensions[ascension].getMinLevel();
    }

    public int getMaxLevel(int ascension) {
        return ascensions[ascension].getMaxLevel();
    }

    public int getMaxTalent(int ascension) {
        return ascensions[ascension].getMaxTalent();
    }


    public boolean hasCharacter(String id) {
        return characters.containsKey(id);
    }

    public CharacterData getCharacter(String id) {
        return characters.get(id);
    }



    public static <T> T readFromJar(final String path, final TypeReference<T> type) {
        final T result;
        final ObjectMapper mapper = new ObjectMapper();
        logger.debug("Attempting to read path '" + path + "' into object of type '" + type + "'");
        try (final InputStream in = GameDataService.class.getResourceAsStream(path)) {
            if(in != null) {
                result = mapper.readValue(in, type);
            } else {
                throw new InitFaultException("Could not read file " + path + " from jar (you probably set the wrong path or forgot to include the file)");
            }
        } catch (IOException e) {
            throw new InitFaultException("Could not read file " + path + " from jar (you probably set the wrong path or forgot to include the file)", e);
        }
        return result;
    }

}
