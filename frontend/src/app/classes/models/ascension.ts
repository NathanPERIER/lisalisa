import { Mapping } from "../typing/mapping";

export interface Ascension {
	costs: Mapping<Number>[];
	props: AscensionProps[];
}

export interface AscensionProps {
	values: Mapping<number>;
	until: number;
}