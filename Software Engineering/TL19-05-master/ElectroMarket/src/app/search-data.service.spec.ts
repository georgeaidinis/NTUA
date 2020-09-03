import { TestBed } from '@angular/core/testing';

import { SearchDataService } from './search-data.service';

describe('SearchDataService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: SearchDataService = TestBed.get(SearchDataService);
    expect(service).toBeTruthy();
  });
});
