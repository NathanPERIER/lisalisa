import { Mapping } from "../typing/mapping"
import { Ascension } from "./ascension"

export interface Character {
	// General data
	name: string;
	desc: string;
	weapon: string;
	rarity: number;
	special: boolean;
	birthday: [number, number] | null;
	region: string;
	vision: string;
	astrolabe: string;
	allegiance: string;
	default_weapon: string;
	// Stats
	base_stats: Mapping<number>;
	curves:     Mapping<string>;
	// Ascensions
	ascensions: Ascension[];
	// Talents, passives, constellations
	talents:  CharacterTalents;
	passives: CharacterPassive[];
	constellations: CharacterConstellation[];
	// Skins
	skins: CharacterSkins;
	// Special dish
	// special_dish: CharacterSpecialDish

}


// Talents ========================================

export interface CharacterTalents {
	normal_attack:    CharacterTalent;
	elemental_skill:  CharacterTalent;
	elemental_burst:  CharacterTalent;
	alternate_sprint: CharacterTalent | null;
}

export interface CharacterTalent {
	name: string;
	desc: string;
	charge_num: number;
	costs: Mapping<number>[];
	stats: CharacterTalentStats;
}

export interface CharacterTalentStats {
	names: string[];
	values: string[][];
}


// Passives ==================================

export interface CharacterPassive {
	name: string;
	desc: string;
	ascension: number;
}


// Constellations ============================

export interface CharacterConstellation {
	name: string;
	desc: string;
}


// Skins =====================================

export interface CharacterSkins {
	default: CharacterSkin;
	alt: CharacterSkin[];
}

export interface CharacterSkin {
	name: string;
	desc: string;
}
