import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewCharacterPageComponent } from './view-character-page.component';

describe('ViewCharacterPageComponent', () => {
  let component: ViewCharacterPageComponent;
  let fixture: ComponentFixture<ViewCharacterPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewCharacterPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewCharacterPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
