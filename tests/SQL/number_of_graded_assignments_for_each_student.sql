SELECT student_id, COUNT(*) AS number_graded
FROM assignments
WHERE state = 'GRADED'
GROUP BY student_id;