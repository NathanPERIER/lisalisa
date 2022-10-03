package lat.elpainauchoco.lisalisa.sanitise;

import lat.elpainauchoco.lisalisa.data.game.ArtifactRarityData;
import lat.elpainauchoco.lisalisa.data.game.GameDataService;
import lat.elpainauchoco.lisalisa.data.user.ArtifactsConf.ArtifactPieceConf;
import lat.elpainauchoco.lisalisa.exceptions.UserConfigException;

import java.util.Map;

public class ArtifactConfSanitiser {

    private final GameDataService gservice;
    private final ArtifactPieceConf piece;
    private final String pieceType;
    private final String pieceId;
    // private final ArtifactSetData artifactSet;
    private ArtifactRarityData rarityData;

    public ArtifactConfSanitiser(final GameDataService gservice, final ArtifactPieceConf piece, final String pieceType, final String pieceId) {
        this.gservice = gservice;
        this.piece = piece;
        this.pieceType = pieceType;
        this.pieceId = pieceId;
        // TODO retrieve set + check
    }

    public void sanitise() {
        sanitiseRarity(piece.getRarity());
        rarityData = gservice.getArtifactRarity(piece.getRarity());
        sanitiseType(piece.getType());
        sanitiseLevel(piece.getLevel());
        sanitiseMainStat(piece.getMainStat(), piece.getType());
        sanitiseSubStats(piece.getSubstats(), piece.getMainStat(), piece.getLevel());
    }

    protected void sanitiseType(final String type) {
        // TODO check that type exists in artifact set
        if(pieceType != null && !pieceType.equals(type)) {
            throw new UserConfigException("Expected type " + pieceType
                    + " for artifact piece " + pieceId
            );
        }
    }

    protected void sanitiseMainStat(final String mainStat, final String type) {
        if(!gservice.getArtifactMainStats(type).contains(mainStat)) {
            throw new UserConfigException("Invalid main stat " + mainStat
                    + " for artifact piece " + pieceId
                    + " of type " + type
            );
        }
    }

    protected void sanitiseRarity(final int rarity) {
        // TODO remove this (actually useless)
        if(rarity < gservice.getMinRarity() || rarity > gservice.getMaxRarity()) {
            throw new UserConfigException("Invalid rarity " + rarity + " for artifact piece " + pieceId);
        }
        // TODO work with artifact data instead
    }

    protected void sanitiseLevel(final int level) {
        if(level < gservice.getMinArtLevel()) {
            throw new UserConfigException("Invalid rarity " + level + " for artifact piece " + pieceId);
        }
        if(level > rarityData.getMaxLevel()) {
            throw new UserConfigException("Invalid rarity " + level
                    + " for artifact piece " + pieceId
                    + " at level " + piece.getLevel()
            );
        }
    }

    protected void sanitiseSubStats(final Map<String, Double> substats, final String mainStat, final int level) {
        if(substats.size() > rarityData.getMaxSubstats()) {
            throw new UserConfigException("Artifact piece " + pieceId + " has too much substats");
        }
        if(substats.size() < rarityData.getMaxSubstats() - (level < 4 ? 1 : 0)) {
            throw new UserConfigException("Artifact piece " + pieceId + " has too little substats");
        }
        if(substats.containsKey(mainStat)) {
            throw new UserConfigException("Artifact piece " + pieceId + " has its main stat as a substat");
        }
        final int maxEnhancements = level/4;
        for(Map.Entry<String, Double> e : substats.entrySet()) {
            if(!rarityData.getSubstats().contains(e.getKey())) {
                throw new UserConfigException("Invalid substat " + e.getKey() + " in artifact piece " + pieceId);
            }
            final float minValue = rarityData.getProps(e.getKey())[0];
            final float maxValue = rarityData.getProps(e.getKey())[1] * (1 + maxEnhancements);
            if(e.getValue() < minValue || e.getValue() > maxValue) {
                throw new UserConfigException("Invalid value " + e.getValue()
                        + " for substat " + e.getKey()
                        + " in artifact piece " + pieceId
                );
            }
        }
    }


}
