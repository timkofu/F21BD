""" Query to crate the structure of the data """

CREATE_STRUCTURE = """
CREATE 
  (`0` :Genre {directorid:'integer',movieid:'integer',genre:'string'}) ,
  (`1` :Director {id:'integer',name:'string',rate:'float',gross:'float',num:'integer'}) ,
  (`2` :Movie {id:'integer',title:'string',year:'date'}) ,
  (`3` :Writer {id:'integer',name:'string'}) ,
  (`4` :Actor {id:'integer',name:'string',sex:'string'}) ,
  (`5` :RunningTime {movieid:'integer',country:'string',addition:'string',time:'integer'}) ,
  (`6` :Rating {movieid:'integer',rank:'float',votes:'integer',distribution:'integer'}) ,
  (`1`)-[:`DIRECTED` ]->(`2`),
  (`3`)-[:`WROTE` {addition:'string'}]->(`2`),
  (`4`)-[:`ACTED_IN` {as_character:'string,',leading:'integer'}]->(`2`),
  (`2`)-[:`HAS_RUNNINGTIME` ]->(`5`),
  (`2`)-[:`HAS_RATING` ]->(`6`),
  (`2`)-[:`IN_GENRE` ]->(`0`),
  (`1`)-[:`DIRECTS` ]->(`0`)
"""
