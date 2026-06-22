BEGIN
   -- Code susceptible de générer une erreur
EXCEPTION
   WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('Aucune donnée trouvée !');
   WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('Erreur non spécifiée : ' || SQLERRM);
END;



RAISE_APPLICATION_ERROR(-20001, 'Erreur personnalisée : valeur invalide');


CREATE OR REPLACE PROCEDURE augmenter_salaire (
   p_emp_id IN NUMBER,
   p_pourcentage IN NUMBER)
IS
BEGIN
   UPDATE employees
   SET salary = salary * (1 + p_pourcentage/100)
   WHERE employee_id = p_emp_id;
   COMMIT;
EXCEPTION
   WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('Erreur lors de la mise à jour du salaire.');
END augmenter_salaire;



CREATE OR REPLACE FUNCTION calculer_prime (
   p_salaire IN NUMBER)
RETURN NUMBER
IS
   v_prime NUMBER;
BEGIN
   v_prime := p_salaire * 0.10;
   RETURN v_prime;
END calculer_prime;


DECLARE
   v_prime NUMBER;
BEGIN
   v_prime := calculer_prime(3000);
   DBMS_OUTPUT.PUT_LINE('Prime calculée : ' || v_prime);
END;
