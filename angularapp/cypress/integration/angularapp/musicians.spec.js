/// <reference types="cypress" />
let url = 'http://localhost:4200/musicians';

context('Location', () => {
  beforeEach(() => {
    cy.visit(url);
  });

  it('should navigate to the first page of the angular app at: ' + url, () => {
    cy.location().should((location) => {
      expect(location.href).to.eq(url);
    });
  });

  it('should print out a message that the new component works', () => {
    cy.get('app-musicians > p').should('contain', 'works!');
  });

  it('gets musicians from api and displays on the page', () => {
    cy.get('app-musicians div').should('contain', 'n/a');
    cy.log('Waiting one second for api call to return...');
    cy.wait(1000);
    cy.get('app-musicians div').should('contain', 'Hetfield');
  });
});
