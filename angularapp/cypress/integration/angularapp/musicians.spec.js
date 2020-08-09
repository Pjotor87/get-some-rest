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
});
