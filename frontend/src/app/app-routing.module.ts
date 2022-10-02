import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ViewCharacterPageComponent } from './components/characters/view-character-page/view-character-page.component';

const routes: Routes = [
    { path: 'u/:user_id/character/:char_id', component: ViewCharacterPageComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
