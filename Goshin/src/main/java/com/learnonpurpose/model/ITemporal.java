package com.learnonpurpose.model;

import java.util.Date;

import javax.persistence.PreUpdate;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

public abstract class ITemporal {
	
	@Temporal(TemporalType.TIMESTAMP)
	Date created = new Date();
	
	@Temporal(TemporalType.TIMESTAMP)
	Date updated = new Date();
	
	@PreUpdate
	public void setLastUpdate() { this.updated = new Date(); }
}
