
export interface CharacterConfig {
	level: number;
	ascension: number;
	normal_attack: number;
	elemental_skill: number;
	elemental_burst: number;
	constellations: number;
	glider: String;
	skin: String;
	limit: CharacterLimitConf;
    // weapon: WeaponConf;
    // artifacts: CharacterArtifactConf;
}

export interface CharacterLimitConf {
	level: number;
	ascension: number;
	normal_attack: number;
	elemental_skill: number;
	elemental_burst: number;
}
