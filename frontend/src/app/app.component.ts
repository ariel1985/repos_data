import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { RepoListComponent } from './repo-list/repo-list.component';
import { RepoDetailsComponent } from './repo-details/repo-details.component';
import { RepoSearchComponent } from './repo-search/repo-search.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RepoListComponent, RepoDetailsComponent, RepoSearchComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
