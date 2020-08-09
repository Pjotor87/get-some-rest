/// <reference types="cypress" />
let url = 'http://localhost:4200';

context('Location', () => {
  beforeEach(() => {
    cy.visit(url);
  });

  it('should navigate to the first page of the angular app at: ' + url, () => {
    cy.location().should((location) => {
      expect(location.href).to.eq(url + '/');
    });
  });

  it('cy.url() - gets the current URL at: ' + url, () => {
    cy.url().should('eq', url + '/');
  });
});
