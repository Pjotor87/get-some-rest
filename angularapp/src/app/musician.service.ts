import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';

import { Musician } from './Musician';

@Injectable({
  providedIn: 'root'
})
export class MusicianService {

  // URL to REST api
  private apiUrl = 'http://localhost:8000/musicians/?format=json';
  //private apiUrl = 'https://get-some-rest.herokuapp.com/musicians/?format=json';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient
  ) { }

  getMusicians(): Observable<Musician[]> {
    return this.http.get<Musician[]>(this.apiUrl)
  }
}
