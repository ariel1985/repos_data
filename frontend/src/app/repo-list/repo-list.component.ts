import { Component } from '@angular/core';
// show the list of repos from repos.service.ts
import { RepoService } from '../repo.service';
import { Repo } from '../repo.service';

@Component({
  selector: 'app-repo-list',
  standalone: true,
  imports: [RepoService],
  templateUrl: './repo-list.component.html',
  styleUrl: './repo-list.component.css'
})
export class RepoListComponent {
  repos: Repo[];

  constructor(private repoService: RepoService) {
    this.repos = repoService.getRepos();
  }

}
