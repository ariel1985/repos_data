import { Injectable } from '@angular/core';

export interface Repo {
  id: number;
  name: string;
  description: string;
  url: string;
  stars: number;
  topics: string[];
  languages: string[];
  owner: string;
}

const REPOS: Repo[] = [
  {
    id: 1,
    name: 'angular',
    description: 'One framework. Mobile & desktop.',
    url: 'http://angular.com',
    stars: 1,
    topics: ['angular'],
    languages: ['typescript'],
    owner: 'angular'
  },
  {
    id: 2,
    name: 'react',
    description: 'A declarative, efficient, and flexible JavaScript library for building user interfaces.',
    url: 'http://react.com',
    stars: 2,
    topics: ['react'],
    languages: ['javascript'],
    owner: 'facebook'
  },
  {
    id: 3,
    name: 'vue',
    description: 'The Progressive JavaScript Framework.',
    url: 'http://vue.com',
    stars: 3,
    topics: ['vue'],
    languages: ['javascript'],
    owner: 'vuejs'
  }
];


@Injectable({
  providedIn: 'root'
})
export class RepoService {

  constructor() { }

  // Get all repos from the service as observable
  getRepos(): Repo[] {
    return REPOS;
  }


  getRepo(id: number): Repo {
    return REPOS.find(repo => repo.id === id) ?? {} as Repo;
  }

  addRepo(repo: Repo): void {
    REPOS.push(repo);
  }

  updateRepo(repo: Repo): void {
    const index = REPOS.findIndex(r => r.id === repo.id);
    REPOS[index] = repo;
  }

  deleteRepo(id: number): void {
    const index = REPOS.findIndex(repo => repo.id === id);
    REPOS.splice(index, 1);
  }

}
