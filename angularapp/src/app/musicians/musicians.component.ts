import { Component, OnInit } from '@angular/core';
import { Musician } from '../Musician';
import { MusicianService } from '../musician.service';

@Component({
  selector: 'app-musicians',
  templateUrl: './musicians.component.html',
  styleUrls: ['./musicians.component.sass']
})
export class MusiciansComponent implements OnInit {

  musicians: Musician[] = [{firstname: "n/a", lastname: "n/a", band: "n/a"}]

  constructor(private musicianService: MusicianService) { }

  ngOnInit(): void {
    this.getMusicians();
  }

  getMusicians(): void {
    this.musicianService.getMusicians()
    .subscribe(musicians => this.musicians = musicians);
  }

}
