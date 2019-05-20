(define
	(domain switch)

	(:predicates (light))

	(:action turnon
		:precondition (not (light))
		:effect (light)
	)
)
