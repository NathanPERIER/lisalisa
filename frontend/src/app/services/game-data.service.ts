import { Injectable } from '@angular/core';
import { Character } from '../classes/models/character';
import { Mapping } from '../classes/typing/mapping';

@Injectable({
  providedIn: 'root'
})
export class GameDataService {

  private chars: Mapping<Character>;

  constructor() {
    this.chars = {};
  }

  public hasCharacter(name: string): boolean {
    return name in this.chars;
  }

  public getCharacter(name: string): Character {
    return this.chars[name];
  }
}
